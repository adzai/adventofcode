defmodule Day1 do
  def part1(file) do
    file
    |> File.read!()
    |> String.trim()
    |> String.split("\n")
    |> Enum.map(&parse_instruction/1)
    |> Enum.reduce(%{pos: 50, count: 0}, fn delta, %{pos: pos, count: count} ->
      new_pos = Integer.mod(pos + delta, 100)
      new_count = if new_pos == 0, do: count + 1, else: count
      %{pos: new_pos, count: new_count}
    end)
    |> Map.get(:count)
  end

  def part2(file) do
    file
    |> File.read!()
    |> String.trim()
    |> String.split("\n")
    |> Enum.map(&parse_instruction/1)
    |> Enum.reduce(%{pos: 50, count: 0}, fn delta, %{pos: pos, count: count} ->
      new_pos = Integer.mod(pos + delta, 100)
      %{pos: new_pos, count: count + count_crosses(pos, delta)}
    end)
    |> Map.get(:count)
  end

  defp parse_instruction("L" <> amount), do: -String.to_integer(amount)
  defp parse_instruction("R" <> amount), do: String.to_integer(amount)

  defp count_crosses(_, 0), do: 0
  defp count_crosses(old_pos, delta) when delta > 0, do: div(old_pos + delta, 100)
  defp count_crosses(old_pos, delta) when old_pos + delta > 0, do: 0
  defp count_crosses(0, delta), do: div(-delta, 100)
  defp count_crosses(old_pos, delta), do: 1 + div(-(old_pos + delta), 100)
end

IO.puts("Part 1: #{Day1.part1("input.txt")}")
IO.puts("Part 2: #{Day1.part2("input.txt")}")
