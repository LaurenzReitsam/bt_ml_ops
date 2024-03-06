#!/bin/sh

PRIV_SA="invoker@bt-pp-dsc-y3gy.iam.gserviceaccount.com"

# shellcheck disable=SC2155
export TOKEN="$(gcloud auth print-identity-token --impersonate-service-account=$PRIV_SA)"
