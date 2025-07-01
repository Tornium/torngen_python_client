defmodule Torngen.Client.Python.MixProject do
  use Mix.Project

  def project do
    [
      app: :torngen_python_client,
      version: version(),
      elixir: "~> 1.16",
      deps: deps()
    ]
  end

  def application do
    [
      extra_applications: [:logger]
    ]
  end

  defp deps do
    [
      # {:torngen, github: "Tornium/torngen", runtime: false}
      {:torngen, path: "../../torngen", runtime: false}
    ]
  end

  defp version do
    case :file.consult(~c"hex_metadata.config") do
      {:ok, data} ->
        {"version", version} = List.keyfind(data, "version", 0)
        version

      _ ->
        version =
          case System.cmd("git", ~w[describe --tags --abbrev=0 --dirty=+dirty]) do
            {version, 0} ->
              version
              |> String.trim()
              |> String.slice(1..-1//1)

            {_, code} ->
              Mix.shell().error("Git exited with code #{code}, falling back to 0.0.0")

              "0.0.0"
          end

        case Version.parse(version) do
          {:ok, %Version{pre: ["pre" <> _ | _]} = version} ->
            to_string(version)

          {:ok, %Version{pre: []} = version} ->
            to_string(version)

          {:ok, %Version{patch: patch, pre: pre} = version} ->
            to_string(%{version | patch: patch + 1, pre: ["dev" | pre]})

          :error ->
            Mix.shell().error("Failed to parse #{version}, falling back to 0.0.0")

            "0.0.0"
        end
    end
  end
end
