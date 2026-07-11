%global tl_name newenviron
%global tl_revision 29331

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Processing an environments body
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/newenviron
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/newenviron.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/newenviron.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package offers tools for collecting and executing an environment's
body.

