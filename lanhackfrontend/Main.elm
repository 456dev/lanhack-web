module Main exposing (main)

import Browser
import Html exposing (Html, text, h1)

type alias Model = ()

type Msg = Msg

main : Program () Model Msg
main =
  Browser.sandbox { init = init, update = update, view = view }

init = ()

update msg model = model

view _ =
  h1 [] [ text "lanhackfrontend" ]
