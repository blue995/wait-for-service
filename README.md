# Wait for a service

This repository contains helpful scripts that wait for a service to be up and ready.

## Supported waiting types

- **netcat**: Simple wait via `nc` to the expected service.
- **consul**: Wait by checking a consul registry and the health of service of this consul registry. 
