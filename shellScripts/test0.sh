#!/bin/bash

function skipline {
  echo
}

echo Hello World!

STR="Hello World!"
echo $STR

echo Date is $(date +%Y%m%d)

skipline

HELLO=Hello
function hello {
  local HELLO=World
  echo $HELLO
}
echo $HELLO
hello
echo $HELLO

skipline

T1="foo"
T2="bar"
if [ $T1 = $T2 ]; then
  echo expression evaluated as true
else
  echo expression evaluated as false
fi
skipline

echo A list of all files in the current directory:
for i in $( ls ); do
  echo item: $i
done
skipline

function e {
  echo $1
}
e Henlo
e Wurpl
skipline
