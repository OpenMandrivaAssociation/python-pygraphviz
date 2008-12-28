%define module	pygraphviz
%define name	python-%{module}
%define version 0.99.1
%define release	%mkrel 2

Summary:	Python interface to Graphviz
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{module}-%{version}.tar.lzma
Patch0:		pygraphviz-0.99.1-fix-str-fmt.patch
License:	BSD
Group:		Development/Python
Url:		https://networkx.lanl.gov/pygraphviz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	graphviz >= 2.0
BuildRequires:	graphviz-devel >= 2.0
%py_requires -d

%description
PyGraphviz is a Python interface to the Graphviz graph layout and
visualization package.

With PyGraphviz, you can create, edit, read, write, and draw graphs
using Python to access the Graphviz graph data structure and layout
algorithms.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p0

%build
%__python setup.py build

%install
%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot}

%__rm -rf %{buildroot}%{_datadir}/doc

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc doc/* examples
%python_sitearch/pygraphviz
%python_sitearch/*.egg-info
