volume_pool = int(input())
first_pipe_hourly = int(input())
second_pipe_hourly = int(input())
hours_off = float(input())

first_pipe_total = first_pipe_hourly * hours_off
second_pipe_total = second_pipe_hourly * hours_off
water_total = first_pipe_total + second_pipe_total

if water_total > volume_pool:
    print(f'For {hours_off:.2f} hours the pool overflows with {water_total - volume_pool:.2f} liters.')
else:
    print(f'The pool is {((water_total / volume_pool) * 100):.2f}% full. Pipe 1:'
          f' {(first_pipe_total / water_total) * 100:.2f}%.'
          f' Pipe 2: {(second_pipe_total / water_total) * 100:.2f}%.')
