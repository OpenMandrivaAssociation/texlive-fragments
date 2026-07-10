%global tl_name fragments
%global tl_revision 79461

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Fragments of LaTeX code
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fragments
License:	collection
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fragments.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fragments.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A collection of fragments of LaTeX code, suitable for inclusion in
packages, or (possibly) in users' documents. Included are: checklab, for
modifying the label checking code at \end{document}; overrightarrow,
defining a doubled over-arrow macro; removefr, for removing 'reset'
relations between counters; and subscript, defining a \textsubscript
command.

