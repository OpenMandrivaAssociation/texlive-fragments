# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/fragments
# catalog-date 2009-01-16 17:12:15 +0100
# catalog-license collection
# catalog-version undef
Name:		texlive-fragments
Version:	20090116
Release:	2
Summary:	Fragments of LaTeX code
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fragments
License:	COLLECTION
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fragments.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fragments.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A collection of fragments of LaTeX code, suitable for inclusion
in packages, or (possibly) in users' documents. Included are: -
checklab, for modifying the label checking code at
\end{document}; - overrightarrow, defining a doubled over-arrow
macro; - removefr, for removing 'reset' relations between
counters; and - subscript, defining a \textsubscript command.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fragments/checklab.tex
%{_texmfdistdir}/tex/latex/fragments/overrightarrow.sty
%{_texmfdistdir}/tex/latex/fragments/removefr.tex
%{_texmfdistdir}/tex/latex/fragments/subscript.sty
%doc %{_texmfdistdir}/doc/latex/fragments/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20090116-2
+ Revision: 752092
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20090116-1
+ Revision: 718502
- texlive-fragments
- texlive-fragments
- texlive-fragments
- texlive-fragments

