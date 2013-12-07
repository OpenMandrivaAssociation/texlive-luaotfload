# revision 31286
# category Package
# catalog-ctan /macros/luatex/generic/luaotfload
# catalog-date 2013-07-11 18:32:48 +0200
# catalog-license gpl2
# catalog-version 2.3a
Name:		texlive-luaotfload
Version:	2.3a
Release:	4
Summary:	OpenType 'loader' for Plain TeX and LaTeX
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
%{_bindir}/luaotfload-tool
%{_bindir}/mkluatexfontdb
%{_texmfdistdir}/scripts/luaotfload/luaotfload-legacy-tool.lua
%{_texmfdistdir}/scripts/luaotfload/luaotfload-tool.lua
%{_texmfdistdir}/scripts/luaotfload/mkcharacters
%{_texmfdistdir}/scripts/luaotfload/mkglyphlist
%{_texmfdistdir}/scripts/luaotfload/mkstatus
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-auxiliary.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-basics-gen.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-basics-nod.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-blacklist.cnf
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-characters.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-colors.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-database.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-extralibs.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-features.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-files.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-fonts-cbk.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-fonts-def.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-fonts-enc.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-fonts-ext.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-fonts-lua.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-fonts-tfm.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-glyphlist.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-legacy-attributes.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-legacy-database.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-legacy-merged.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-legacy.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-letterspace.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-loaders.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-merged.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-override.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-status.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-typo-krn.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload.sty
%doc %{_texmfdistdir}/doc/luatex/luaotfload/NEWS
%doc %{_texmfdistdir}/doc/luatex/luaotfload/README
%doc %{_texmfdistdir}/doc/luatex/luaotfload/filegraph.pdf
%doc %{_texmfdistdir}/doc/luatex/luaotfload/luaotfload.pdf
%doc %{_mandir}/man1/luaotfload-tool.1*
%doc %{_texmfdistdir}/doc/man/man1/luaotfload-tool.man1.pdf
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
    ln -sf %{_texmfdistdir}/scripts/luaotfload/luaotfload-tool.lua luaotfload-tool
    ln -sf luaotfload-tool mkluatexfontdb
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
