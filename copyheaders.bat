if not exist "..\include" mkdir "..\include"
if not exist "..\include\lua" mkdir "..\include\lua"

for %%H in (
    lua.h
    lualib.h
    lauxlib.h
    luaconf.h
) do (
    copy "..\%%H" "..\include\lua\%%H"
)