def fixCrash():
    """
    @author Muffinized / Kenneth

    DO NOT EDIT THIS SECTION

    This code is to fix the crash many students have
    been experiencing. This is due to the hitboxes of
    many half-textured boxes intersecting poorly with
    the hitbox of the player.
    """
    import site
    import os
    import base64
    # print( site.getsitepackages())
    path = site.getsitepackages()[0] + os.sep + "arcade" + os.sep
    lol = "IiIiCkZ1bmN0aW9ucyBmb3IgY2FsY3VsYXRpbmcgZ2VvbWV0cnkuCiIiIgppbXBvcnQgdGltZQpmcm9tIHR5cGluZyBpbX" \
          "BvcnQgY2FzdAoKZnJvbSBhcmNhZGUgaW1wb3J0IFBvaW50TGlzdAoKCgpfUFJFQ0lTSU9OID0gMgoKCmRlZiBhcmVfcG9s" \
          "eWdvbnNfaW50ZXJzZWN0aW5nKHBvbHlfYTogUG9pbnRMaXN0LAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICBwb2" \
          "x5X2I6IFBvaW50TGlzdCkgLT4gYm9vbDoKICAgICIiIgogICAgUmV0dXJuIFRydWUgaWYgdHdvIHBvbHlnb25zIGludGVy" \
          "c2VjdC4KCiAgICA6cGFyYW0gUG9pbnRMaXN0IHBvbHlfYTogTGlzdCBvZiBwb2ludHMgdGhhdCBkZWZpbmUgdGhlIGZpcn" \
          "N0IHBvbHlnb24uCiAgICA6cGFyYW0gUG9pbnRMaXN0IHBvbHlfYjogTGlzdCBvZiBwb2ludHMgdGhhdCBkZWZpbmUgdGhl" \
          "IHNlY29uZCBwb2x5Z29uLgogICAgOlJldHVybnM6IFRydWUgb3IgZmFsc2UgZGVwZW5kaW5nIGlmIHBvbHlnb25zIGludG" \
          "Vyc2VjdAoKICAgIDpydHlwZSBib29sOgogICAgIiIiCgogICAgZm9yIHBvbHlnb24gaW4gKHBvbHlfYSwgcG9seV9iKToK" \
          "CiAgICAgICAgZm9yIGkxIGluIHJhbmdlKGxlbihwb2x5Z29uKSk6CiAgICAgICAgICAgIGkyID0gKGkxICsgMSkgJSBsZW" \
          "4ocG9seWdvbikKICAgICAgICAgICAgcHJvamVjdGlvbl8xID0gcG9seWdvbltpMV0KICAgICAgICAgICAgcHJvamVjdGlv" \
          "bl8yID0gcG9seWdvbltpMl0KCiAgICAgICAgICAgIG5vcm1hbCA9IChwcm9qZWN0aW9uXzJbMV0gLSBwcm9qZWN0aW9uXz" \
          "FbMV0sCiAgICAgICAgICAgICAgICAgICAgICBwcm9qZWN0aW9uXzFbMF0gLSBwcm9qZWN0aW9uXzJbMF0pCgogICAgICAg" \
          "ICAgICBtaW5fYSwgbWF4X2EsIG1pbl9iLCBtYXhfYiA9IChOb25lLCkgKiA0CgogICAgICAgICAgICBmb3IgcG9seSBpbi" \
          "Bwb2x5X2E6CiAgICAgICAgICAgICAgICBwcm9qZWN0ZWQgPSBub3JtYWxbMF0gKiBwb2x5WzBdICsgbm9ybWFsWzFdICog" \
          "cG9seVsxXQoKICAgICAgICAgICAgICAgIGlmIG1pbl9hIGlzIE5vbmUgb3IgcHJvamVjdGVkIDwgbWluX2E6CiAgICAgIC" \
          "AgICAgICAgICAgICAgbWluX2EgPSBwcm9qZWN0ZWQKICAgICAgICAgICAgICAgIGlmIG1heF9hIGlzIE5vbmUgb3IgcHJv" \
          "amVjdGVkID4gbWF4X2E6CiAgICAgICAgICAgICAgICAgICAgbWF4X2EgPSBwcm9qZWN0ZWQKCiAgICAgICAgICAgIGZvci" \
          "Bwb2x5IGluIHBvbHlfYjoKICAgICAgICAgICAgICAgIHByb2plY3RlZCA9IG5vcm1hbFswXSAqIHBvbHlbMF0gKyBub3Jt" \
          "YWxbMV0gKiBwb2x5WzFdCgogICAgICAgICAgICAgICAgaWYgbWluX2IgaXMgTm9uZSBvciBwcm9qZWN0ZWQgPCBtaW5fYj" \
          "oKICAgICAgICAgICAgICAgICAgICBtaW5fYiA9IHByb2plY3RlZAogICAgICAgICAgICAgICAgaWYgbWF4X2IgaXMgTm9u" \
          "ZSBvciBwcm9qZWN0ZWQgPiBtYXhfYjoKICAgICAgICAgICAgICAgICAgICBtYXhfYiA9IHByb2plY3RlZAogICAgICAgIC" \
          "AgICB0cnk6CiAgICAgICAgICAgICAgICBpZiBjYXN0KGZsb2F0LCBtYXhfYSkgPD0gY2FzdChmbG9hdCwgbWluX2IpIG9y" \
          "IGNhc3QoZmxvYXQsIG1heF9iKSA8PSBjYXN0KGZsb2F0LCBtaW5fYSk6CiAgICAgICAgICAgICAgICAgICAgcmV0dXJuIE" \
          "ZhbHNlCiAgICAgICAgICAgIGV4Y2VwdDoKICAgICAgICAgICAgICAgIHJldHVybiBGYWxzZQoKICAgIHJldHVybiBUcnVl" \
          "CgoKZGVmIGlzX3BvaW50X2luX3BvbHlnb24oeCwgeSwgcG9seWdvbl9wb2ludF9saXN0KToKICAgICIiIgogICAgVXNlIH" \
          "JheS10cmFjaW5nIHRvIHNlZSBpZiBwb2ludCBpcyBpbnNpZGUgYSBwb2x5Z29uCgogICAgQXJnczoKICAgICAgICB4Ogog" \
          "ICAgICAgIHk6CiAgICAgICAgcG9seWdvbl9wb2ludF9saXN0OgoKICAgIFJldHVybnM6IGJvb2wKCiAgICAiIiIKICAgIG" \
          "4gPSBsZW4ocG9seWdvbl9wb2ludF9saXN0KQogICAgaW5zaWRlID0gRmFsc2UKICAgIGlmIG4gPT0gMDoKICAgICAgICBy" \
          "ZXR1cm4gRmFsc2UKCiAgICBwMXgsIHAxeSA9IHBvbHlnb25fcG9pbnRfbGlzdFswXQogICAgZm9yIGkgaW4gcmFuZ2Uobi" \
          "ArIDEpOgogICAgICAgIHAyeCwgcDJ5ID0gcG9seWdvbl9wb2ludF9saXN0W2kgJSBuXQogICAgICAgIGlmIHkgPiBtaW4o" \
          "cDF5LCBwMnkpOgogICAgICAgICAgICBpZiB5IDw9IG1heChwMXksIHAyeSk6CiAgICAgICAgICAgICAgICBpZiB4IDw9IG" \
          "1heChwMXgsIHAyeCk6CiAgICAgICAgICAgICAgICAgICAgaWYgcDF5ICE9IHAyeToKICAgICAgICAgICAgICAgICAgICAg" \
          "ICAgeGludHMgPSAoeSAtIHAxeSkgKiAocDJ4IC0gcDF4KSAvIChwMnkgLSBwMXkpICsgcDF4CiAgICAgICAgICAgICAgIC" \
          "AgICAgIyBub2luc3BlY3Rpb24gUHlVbmJvdW5kTG9jYWxWYXJpYWJsZQogICAgICAgICAgICAgICAgICAgIGlmIHAxeCA9" \
          "PSBwMnggb3IgeCA8PSB4aW50czoKICAgICAgICAgICAgICAgICAgICAgICAgaW5zaWRlID0gbm90IGluc2lkZQogICAgIC" \
          "AgIHAxeCwgcDF5ID0gcDJ4LCBwMnkKCiAgICByZXR1cm4gaW5zaWRlCg=="
          # This is not a virus, you can use base64decoder.com to understand what this is.
    with open(path + 'geometry_python.py', 'w') as fill:
        okay = base64.b64decode(lol).__str__()
        fill.write(okay.replace("\\n", "\n").removeprefix("b'").removesuffix("'"))

        fill.close()
        # print("Code has been successfully patched. (Collision fix by Muffy")

