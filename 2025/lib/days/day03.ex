defmodule Day03 do
  def part1(file) do
    file
    |> Aoc.read_lines()
    |> Enum.map(&compute_joltage(&1, 2))
    |> Enum.sum()
  end

  def part2(file) do
    file
    |> Aoc.read_lines()
    |> Enum.map(&compute_joltage(&1, 12))
    |> Enum.sum()
  end

  defp compute_joltage(line, n) do
    digits = line |> String.graphemes() |> Enum.map(&String.to_integer/1) |> List.to_tuple()
    len = tuple_size(digits)

    {result, _pos} =
      Enum.reduce(0..(n - 1), {0, 0}, fn i, {acc, left_bound} ->
        right_bound = len - (n - i - 1)
        {max_val, max_pos} = find_leftmost_max(digits, left_bound, right_bound)
        {acc * 10 + max_val, max_pos + 1}
      end)

    result
  end

  defp find_leftmost_max(digits, left, right) do
    Enum.reduce(left..(right - 1), {-1, -1}, fn pos, {best_val, best_pos} ->
      val = elem(digits, pos)
      if val > best_val, do: {val, pos}, else: {best_val, best_pos}
    end)
  end
end
