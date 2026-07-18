%global tl_name luaotfload
%global tl_revision 74324
%global tl_bin_links luaotfload-tool:%{_texmfdistdir}/scripts/luaotfload/luaotfload-tool.lua

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.29
Release:	%{tl_revision}.1
Summary:	OpenType loader for Plain TeX and LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/generic/luaotfload
License:	gpl2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luaotfload.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luaotfload.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luaotfload.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(lm)
Requires:	texlive(lua-alt-getopt)
Requires:	texlive(lua-uni-algos)
Requires:	texlive(lualibs)
Requires:	texlive(luaotfload.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
The package adopts the TrueType/OpenType Font loader code provided in
ConTeXt, and adapts it to use in Plain TeX and LaTeX. It works under
LuaLaTeX only.

