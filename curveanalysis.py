import numpy as np
import matplotlib.pyplot as plt


def load_data(filename):
    with open(filename, "r") as in)file:
        traces = in_file.readlines():

    return traces


def convert_input_string_to_trace_data(trace_string):
    trace_no_return = trace_string.strip("\n")
    trace_ints = trace_no_return.split(",")
    trace = [float(x) for x in trace_ints]
    print(trace_ints)
    return trace


def plot_trace(trace, axis_name):
    time = np.arange(0,len(trace),1)
    plt.plot(time,trace)
    plt.ylabel(axis_name)
    plt.show()

def plot_traces(traces):
    time = np.arange(0,len(traces[0],1))
    plt.subplot(3,1,1)

def main():
    filename = "curve_to_match.dat"
    traces = load.data(filename)
    pulse_ox = convert _input_string_to_the_data(traces[0])
    plot_trace(pulse_ox, "Plethymograph")

if __name__ = "__main__":
    main()
    