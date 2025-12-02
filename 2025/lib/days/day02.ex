defmodule Day02 do
  def part1(file) do
    file
    |> File.read!()
    |> String.trim()
    |> String.split(",")
    |> Enum.flat_map(&parse_range/1)
    |> Enum.reduce(0, fn id, sum ->
      if repeated_halves?(id), do: sum + id, else: sum
    end)
  end

  def part2(file) do
    file
    |> File.read!()
    |> String.trim()
    |> String.split(",")
    |> Stream.flat_map(&parse_range/1)
    |> Enum.reduce(0, fn id, sum ->
      if is_repeated_pattern?(id), do: sum + id, else: sum
    end)
  end

  defp is_repeated_pattern?(n) do
    s = Integer.to_string(n)
    len = String.length(s)

    1..div(len, 2)//1
    |> Stream.filter(&(rem(len, &1) == 0))
    |> Enum.any?(fn pattern_len ->
      s == String.duplicate(String.slice(s, 0, pattern_len), div(len, pattern_len))
    end)
  end

  defp parse_range(range) do
    [start, stop] = String.split(range, "-")
    String.to_integer(start)..String.to_integer(stop)
  end

  defp repeated_halves?(n) do
    s = Integer.to_string(n)
    {first, second} = String.split_at(s, div(String.length(s), 2))
    first == second
  end
end
