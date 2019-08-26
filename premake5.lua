workspace "lua"
    language        "C++"
    kind            "StaticLib"
    targetdir       "build/%{cfg.action}/bin/%{cfg.longname}"
    objdir          "build/%{cfg.action}/obj/%{prj.name}/%{cfg.longname}"
    --characterset    "MBCS"
    --cppdialect      "c++17"
    systemversion   "latest"
    staticruntime   "on"

    postbuildcommands {
        "py publish.py %{cfg.platform} %{cfg.buildcfg} %{cfg.action}"
    }

    defines {
        "_LIB"
    }

    platforms {
        "Win32",
        "x64",
    }

    filter "platforms:Win32"
        architecture "x86"
        defines {
            "WIN32"
        }
    
    filter "platforms:x64"
        architecture "x64"
    
    filter {}

    configurations {
        "Debug",
        "Release",
    }
    
    flags {
        "MultiProcessorCompile"
    }

    filter "configurations:Debug"
        symbols "on"

        defines {
            "_DEBUG"
        }
    
    filter "configurations:Release"
        optimize "on"

        defines {
            "NDEBUG"
        }
    
        flags {
            "NoIncrementalLink",
            "LinkTimeOptimization",
        }
    
    filter {}

    project "lua"

        files {
            "*.c",
            "*.h",
            "*.py"
        }

        excludes {
            "lua.c",
            "onelua.c"
        }

        filter "files:*.c"
            compileas "C++"