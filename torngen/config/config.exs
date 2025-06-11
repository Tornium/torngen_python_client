import Config

config :torngen,
  file: "../openapi.json",
  out_dir: "../generated",
  generator: :python
