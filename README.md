# SUFMS---SAR_USV_Fleet_Management_System
A work about a system of relatively small, cheap and expendable marine SAR USV's, especially management of fleet of those.


# Overview

SUFMS aims to coordinate a fleet of relatively small, cheap, and expendable USVs to maximize the probability of finding castaways or missing vessels in the shortest possible time. The system is built around optimal search theory (Koopman) and Bayesian probability mapping, adapted for autonomous multi-vehicle coordination.

# Goals


Implement an optimal search algorithm based on Koopman search theory with Bayesian map updates
Coordinate a fleet USVs with a centralized command system and local autonomy
Handle dynamic replanning in response to unit loss, communication failure, or changing conditions
Provide realistic simulation of both the search environment and the search targets


# Architecture

The project is developed in layers, each buildable and testable independently:

Castaway simulation — models castaways in the sea, including Brownian motion, group drift tendencies, ocean currents and wind influence, and survival probability over time based on water temperature, wave height, and time in water.

Fleet simulation — models USV movement, sensor coverage (EO/IR), and communication with the central server.

Search coordination — central command system implementing Koopman-based search path planning, Voronoi area decomposition for fleet sector assignment, and dynamic replanning on unit loss or new information.

Communication simulation — models message exchange between USVs and the command server, including latency, packet loss, and disconnection handling.

# Current Status

Early development. Castaway simulation in progress.

# Tech Stack


Python



# License

MIT License — see LICENSE for details.
Hardware designs, if any, will be released under CERN OHL.
