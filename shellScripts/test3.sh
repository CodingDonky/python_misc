#!/bin/bash

# For loops

echo ""
for command in ls pwd Date
do
  echo "----------$command----------"
  $command
done
echo ""

echo "----------Directories located in .----------"
for item in *
do
  if [ -d $item ]
  then
    echo $item
  fi
done
echo ""

echo "----------Files located in .----------"
for item in *
do
  if [ -f $item ]
  then
    echo $item
  fi
done
echo ""
