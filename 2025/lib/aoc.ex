defmodule Aoc do
  def run_day(day) do
    padded = day |> Integer.to_string() |> String.pad_leading(2, "0")
    module = String.to_atom("Elixir.Day#{padded}")
    file = "inputs/day#{padded}.txt"

    case Code.ensure_loaded(module) do
      {:module, _} ->
        IO.puts("Part 1: #{module.part1(file)}")
        IO.puts("Part 2: #{module.part2(file)}")

      {:error, _} ->
        IO.puts("Day #{padded} not implemented")
    end
  end

  def read_lines(file) do
    file
    |> File.read!()
    |> String.trim()
    |> String.split("\n")
  end
end
