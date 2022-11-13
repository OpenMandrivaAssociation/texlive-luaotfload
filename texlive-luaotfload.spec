Name:		texlive-luaotfload
Version:	64616
Release:	1
Summary:	OpenType 'loader' for Plain TeX and LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/luatex/generic/luaotfload
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luaotfload.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luaotfload.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luaotfload.source.r%{version}.tar.xz
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
%{_texmfdistdir}/scripts/luaotfload
%{_texmfdistdir}/tex/luatex/luaotfload
%doc %{_texmfdistdir}/doc/luatex/luaotfload
%doc %{_mandir}/man1/luaotfload-tool.1*
%doc %{_texmfdistdir}/doc/man/man1/luaotfload-tool.man1.pdf
%doc %{_mandir}/man5/luaotfload.conf.5*
%doc %{_texmfdistdir}/doc/man/man5/luaotfload.conf.man5.pdf
#- source
%doc %{_texmfdistdir}/source/luatex/luaotfload

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/luaotfload/luaotfload-tool.lua luaotfload-tool
ln -sf luaotfload-tool mkluatexfontdb
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1 %{buildroot}%{_mandir}/man5
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man5/*.5 %{buildroot}%{_mandir}/man5
