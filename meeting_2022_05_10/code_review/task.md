# Task description

## General description

Design a software module for handling data packages from a fitness tracker. The module get data packages as a tuple. The module gets data on some event (e.g. user presses the button).

## Expected input

The order of data in the tuple is described below:\  
(time, number of completed steps from the last call, pulse)

## Expected output

The module should print the following properties in stdout:

- Summary of the steps
- Completed distance
- Burned calories

## Possible errors in the package

- The data package can have a smaller or larger length
- Some of the data in the package is None
- The time property in the received package is smaller than in the previous one

## Technical aspects

- The packages should be stored in the list of dictionaries
- The result list should not have the wrong packages