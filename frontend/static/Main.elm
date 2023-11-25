port module Main exposing (main)

import Browser
import Html exposing (Html, text, h1)
import Json.Encode as JE
import Json.Decode as JD
import Platform.Sub as Sub
import Platform.Cmd as Cmd

port receiveSocketMsg : (JD.Value -> msg) -> Sub msg
port sendSocketCommand : JE.Value -> Cmd msg

type alias Model = ()

type Msg = Msg

main : Program () Model Msg
main =
  Browser.element { init = init, subscriptions = always Sub.none, update = update, view = view }

init _ = ((), Cmd.none)

update msg model = (model, Cmd.none)

view _ =
  h1 [] [ text "lanhackfrontend" ]
