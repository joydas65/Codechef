import sys
input = sys.stdin.readline


def max_edges_in_dag(total_vertices, num_sources, num_sinks):
    both_source_and_sink = max(0, num_sources + num_sinks - total_vertices)
    pure_sources = num_sources - both_source_and_sink
    pure_sinks = num_sinks - both_source_and_sink
    middle = total_vertices - num_sources - num_sinks + both_source_and_sink

    edges_from_sources = pure_sources * (middle + pure_sinks)
    edges_within_middle = middle * (middle - 1) // 2
    edges_to_sinks = middle * pure_sinks

    return edges_from_sources + edges_within_middle + edges_to_sinks


T = int(input())
output = []
for _ in range(T):
    N, K, L = map(int, input().split())
    output.append(str(max_edges_in_dag(N, K, L)))

sys.stdout.write("\n".join(output) + "\n")
