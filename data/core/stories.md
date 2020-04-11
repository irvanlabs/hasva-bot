## senang
* greet
  - utter_greet
  - utter_name
* mood_great
  - utter_happy

## New Story

* mood_unhappy
    - utter_cheer_up
    - utter_did_that_help
* affirm
    - utter_happy

## senang path 2
* greet
  - utter_hello
* mood_great
  - utter_happy

## senang path 3
* greet
  - utter_hello
* salam_kenal
  - utter_i_can_help

## tanya
* how_can_do
  - utter_how_can_do

## sad pattern 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad pattern 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## question_state
* question_state
  - utter_state

## pattern thx
* thanks
  - utter_thanks

## pattern age
* how_old
  - utter_how_old

## gender
* gender
  - utter_gender

## pertanyaan sepele
* question_general
  - utter_question_general

## user asks for something out of scope
* out_of_scope
  - utter_default
  - utter_how_can_do
