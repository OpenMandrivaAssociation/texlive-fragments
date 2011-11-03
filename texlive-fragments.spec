# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/fragments
# catalog-date 2009-01-16 17:12:15 +0100
# catalog-license collection
# catalog-version undef
Name:		texlive-fragments
Version:	20090116
Release:	1
Summary:	Fragments of LaTeX code
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fragments
License:	COLLECTION
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fragments.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fragments.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
A collection of fragments of LaTeX code, suitable for inclusion
in packages, or (possibly) in users' documents. Included are: -
checklab, for modifying the label checking code at
\end{document}; - overrightarrow, defining a doubled over-arrow
macro; - removefr, for removing 'reset' relations between
counters; and - subscript, defining a \textsubscript command.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fragments/checklab.tex
%{_texmfdistdir}/tex/latex/fragments/overrightarrow.sty
%{_texmfdistdir}/tex/latex/fragments/removefr.tex
%{_texmfdistdir}/tex/latex/fragments/subscript.sty
%doc %{_texmfdistdir}/doc/latex/fragments/README
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
