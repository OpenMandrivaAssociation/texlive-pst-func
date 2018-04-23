Name:		texlive-pst-func
Version:	0.89
Release:	1
Summary:	PSTricks package for plotting mathematical functions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-func
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-func.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-func.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is built for use with PSTricks. It provides macros
for plotting and manipulating various mathematical functions:
polynomials and their derivatives f(x)=an*x^n+an-1*x^(n-
1)+...+a0 defined by the coefficients a0 a1 a2 ... and the
derivative order; the Fourier sum f(x) = a0/2+a1cos(omega
x)+...+b1sin(omega x)+... defined by the coefficients a0 a1 a2
... b1 b2 b3 ...; the Bessel function defined by its order; the
Gauss function defined by sigma and mu; Bezier curves from
order 1 (two control points) to order 9 (10 control points);
the superellipse function (the Lame curve); Chebyshev
polynomials of the first and second kind; the Thomae (or
popcorn) function; the Weierstrass function; various
integration-derived functions; normal, binomial, poisson,
gamma, chi-squared, student's t, F, beta, Cauchy and Weibull
distribution functions and the Lorenz curve; the zeroes of a
function, or the intermediate point of two functions; the
Vasicek function for describing the evolution of interest
rates; and implicit functions. The plots may be generated as
volumes of rotation about the X-axis, as well.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pst-func
%{_texmfdistdir}/tex/generic/pst-func
%{_texmfdistdir}/tex/latex/pst-func
%doc %{_texmfdistdir}/doc/generic/pst-func

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}
