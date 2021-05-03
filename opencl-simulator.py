#!/usr/bin/env python3

# @Author: GeorgeRaven <archer>
# @Date:   2021-05-03T16:04:49+01:00
# @Last modified by:   archer
# @Last modified time: 2021-05-03T17:51:26+01:00
# @License: please see LICENSE file in project root

import sys
import numpy as np  # https://pypi.org/project/numpy/
import configargparse  # https://pypi.org/project/ConfigArgParse/


def main(args):
    # create data and generate predefined id arrays
    vector = np.arange(-(2**(args["scale"]-1)), 2**(args["scale"]-1))
    output = np.zeros(vector.shape)
    global_ids = np.arange(len(vector))
    group_ids = np.arange(2**args["group_scale"])
    # shuffle groups and vector
    np.random.shuffle(vector)
    np.random.shuffle(global_ids)
    np.random.shuffle(group_ids)
    # now using this information mimic opencl behaviour
    opencl(_vector=vector,
           _output=output,
           _global_ids=global_ids,
           _group_ids=group_ids)


def opencl(_vector, _output, _group_ids, _global_ids):
    """Call OpenCL mimic."""
    print("Input Elements:", _vector.size)
    print("Local/ Group Size:", _group_ids.size)

    def get_global_size(_i: int):
        # if this errors you have called the opencl like tuple wrong try 0
        return (_vector.size,)[_i]

    def get_local_size(_i: int):
        # if this errors you have called the opencl like tuple wrong try 0
        return (_group_ids.size,)[_i]

    _id = 0
    _gid = 0
    while(_id < _vector.size):

        def get_group_id(_i: int):
            # if this errors you have called the opencl wrong
            return (_gid,)[_i]

        _scratch = np.zeros(_group_ids.size)

        for _lid in _group_ids:

            def get_global_id(_i: int):
                # if this errors you have called the opencl wrong
                return (_global_ids[_id],)[_i]

            def get_local_id(_i: int):
                # if this errors you have called the opencl wrong
                return (_lid,)[_i]

            def kernel(A: np.ndarray, B: np.ndarray, scratch: np.ndarray):
                """Simulate OpenCL Kernel."""
                id = get_global_id(0)
                lid = get_local_id(0)
                N = get_global_size(0)
                L = get_local_size(0)
                # YOUR CODE GOES FROM HERE
                B[id] = A[id]
                # TO HERE

            kernel(A=_vector, B=_output, scratch=_scratch)

            _id += 1
        _gid += 1

    print("A:", _vector)
    print("Stats: A.max={}, A.min={}, A.std={}".format(
        _vector.max(),
        _vector.min(),
        np.std(_vector)
    ))
    print("B:", _output)


def arg_handler(argv=[], description=None):
    """Quick argument handler just to make everything easier to work with."""
    description = description if description is not None else "api args"
    parser = configargparse.ArgumentParser(description=description)

    parser.add_argument("-s", "--scale",
                        type=int,
                        default=7,
                        env_var="PY_KERNEL_SCALE",
                        help="Scale (S) in N=2^S for vector length.")
    parser.add_argument("-g", "--group-scale",
                        type=int,
                        default=2,
                        env_var="PY_KERNEL_GROUP_SCALE",
                        help="Group scale (G) in L=2^G for local/ group size.")

    args = vars(parser.parse_args(argv))
    return args


if __name__ == "__main__":
    main(arg_handler(sys.argv[1:],
                     description="Python Kernel Experimenter."))
