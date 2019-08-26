import os
import sys
import shutil

platform = sys.argv[1]
buildcfg = sys.argv[2]
compiler = sys.argv[3]

def log(msg):
    print("[publish.py] " + msg)

log("Publishing for " + platform + "/" + buildcfg + " (" + compiler + ")")

include_headers = [
    "lua.h",
    "lualib.h",
    "lauxlib.h",
    "luaconf.h"
]

os.makedirs("publish\\include\\lua", exist_ok=True)
for name in include_headers:
    shutil.copy2(name, os.path.join("publish\\include\\lua\\", name))

# os.path.exists
def cp(src, dst):
    if os.path.exists(src):
        shutil.copy2(src, dst)
        return True
    
    return False

# Copy libs ...

if platform == "Win32":
    dst_dir = os.path.join("publish\\lib", compiler, "x86")
    os.makedirs(dst_dir, exist_ok=True)
    if buildcfg == "Debug":
        cp(os.path.join("build", compiler, "bin", buildcfg, platform, "lua.lib"), os.path.join(dst_dir, "luaD.lib"))
        cp(os.path.join("build", compiler, "bin", buildcfg, platform, "lua.pdb"), os.path.join(dst_dir, "luaD.pdb"))
    elif buildcfg == "Release":
        cp(os.path.join("build", compiler, "bin", buildcfg, platform, "lua.lib"), os.path.join(dst_dir, "lua.lib"))
        cp(os.path.join("build", compiler, "bin", buildcfg, platform, "lua.pdb"), os.path.join(dst_dir, "lua.pdb"))
    else:
        log("Unknown build configuration: " + buildcfg)
        exit(1)
elif platform == "x64":
    dst_dir = os.path.join("publish\\lib", compiler, "x64")
    os.makedirs(dst_dir, exist_ok=True)
    if buildcfg == "Debug":
        cp(os.path.join("build", compiler, "bin", buildcfg, platform, "lua.lib"), os.path.join(dst_dir, "luaD.lib"))
        cp(os.path.join("build", compiler, "bin", buildcfg, platform, "lua.pdb"), os.path.join(dst_dir, "luaD.pdb"))
    elif buildcfg == "Release":
        cp(os.path.join("build", compiler, "bin", buildcfg, platform, "lua.lib"), os.path.join(dst_dir, "lua.lib"))
        cp(os.path.join("build", compiler, "bin", buildcfg, platform, "lua.pdb"), os.path.join(dst_dir, "lua.pdb"))
    else:
        log("Unknown build configuration: " + buildcfg)
        exit(1)
else:
    log("Unknown platform: " + platform)
    exit(1)

log("Completed")