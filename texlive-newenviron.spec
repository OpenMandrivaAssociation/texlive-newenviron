# revision 29331
# category Package
# catalog-ctan /macros/latex/contrib/newenviron
# catalog-date 2013-03-10 16:42:24 +0100
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-newenviron
Version:	1.0
Release:	5
Summary:	Processing an environment's body
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/newenviron
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newenviron.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newenviron.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package offers tools for collecting and executing an
environment's body.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/newenviron/newenviron.sty
%doc %{_texmfdistdir}/doc/latex/newenviron/README
%doc %{_texmfdistdir}/doc/latex/newenviron/newenviron-examples.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
