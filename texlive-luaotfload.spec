# revision 22165
# category Package
# catalog-ctan /macros/luatex/generic/luaotfload
# catalog-date 2011-02-20 17:28:20 +0100
# catalog-license gpl2
# catalog-version 1.24
Name:		texlive-luaotfload
Version:	1.24
Release:	1
Summary:	OpenType layout system for Plain TeX and LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/luatex/generic/luaotfload
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luaotfload.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luaotfload.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luaotfload.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-luaotfload.bin = %{EVRD}

%description
The package adopts the TrueType/OpenType Font loader code
provided in ConTeXt, and adapts it to use in Plain TeX and
LaTeX.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/mkluatexfontdb
%{_texmfdistdir}/scripts/luaotfload/mkluatexfontdb.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload.sty
%{_texmfdistdir}/tex/luatex/luaotfload/otfl-blacklist.cnf
%{_texmfdistdir}/tex/luatex/luaotfload/otfl-data-con.lua
%{_texmfdistdir}/tex/luatex/luaotfload/otfl-font-cid.lua
%{_texmfdistdir}/tex/luatex/luaotfload/otfl-font-clr.lua
%{_texmfdistdir}/tex/luatex/luaotfload/otfl-font-def.lua
%{_texmfdistdir}/tex/luatex/luaotfload/otfl-font-dum.lua
%{_texmfdistdir}/tex/luatex/luaotfload/otfl-font-ini.lua
%{_texmfdistdir}/tex/luatex/luaotfload/otfl-font-map.lua
%{_texmfdistdir}/tex/luatex/luaotfload/otfl-font-nms.lua
%{_texmfdistdir}/tex/luatex/luaotfload/otfl-font-ota.lua
%{_texmfdistdir}/tex/luatex/luaotfload/otfl-font-otb.lua
%{_texmfdistdir}/tex/luatex/luaotfload/otfl-font-otc.lua
%{_texmfdistdir}/tex/luatex/luaotfload/otfl-font-otd.lua
%{_texmfdistdir}/tex/luatex/luaotfload/otfl-font-otf.lua
%{_texmfdistdir}/tex/luatex/luaotfload/otfl-font-oti.lua
%{_texmfdistdir}/tex/luatex/luaotfload/otfl-font-otn.lua
%{_texmfdistdir}/tex/luatex/luaotfload/otfl-font-ott.lua
%{_texmfdistdir}/tex/luatex/luaotfload/otfl-font-tfm.lua
%{_texmfdistdir}/tex/luatex/luaotfload/otfl-font-xtx.lua
%{_texmfdistdir}/tex/luatex/luaotfload/otfl-luat-dum.lua
%{_texmfdistdir}/tex/luatex/luaotfload/otfl-luat-ovr.lua
%{_texmfdistdir}/tex/luatex/luaotfload/otfl-node-dum.lua
%{_texmfdistdir}/tex/luatex/luaotfload/otfl-node-inj.lua
%doc %{_texmfdistdir}/doc/luatex/luaotfload/NEWS
%doc %{_texmfdistdir}/doc/luatex/luaotfload/README
%doc %{_texmfdistdir}/doc/luatex/luaotfload/luaotfload.pdf
#- source
%doc %{_texmfdistdir}/source/luatex/luaotfload/Makefile
%doc %{_texmfdistdir}/source/luatex/luaotfload/luaotfload.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/luaotfload/mkluatexfontdb.lua mkluatexfontdb
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
