%define module	pygraphviz
%define name	python-%{module}
%define version 0.99.1
%define release	%mkrel 2

Summary:	Python interface to Graphviz
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{module}-%{version}.tar.lzma
License:	BSD
Group:		Development/Python
Url:		https://networkx.lanl.gov/pygraphviz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	graphviz >= 2.0
Requires:	python >= 2.4
BuildRequires:	graphviz-devel >= 2.0
BuildRequires:	python-devel >= 2.4

%description
PyGraphviz is a Python interface to the Graphviz graph layout and
visualization package.

With PyGraphviz, you can create, edit, read, write, and draw graphs
using Python to access the Graphviz graph data structure and layout
algorithms.

%prep
%setup -q -n %{module}-%{version}

%build

%install
%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot} --record=FILELIST

%clean
%__rm -rf %{buildroot}

%files -f FILELIST
%defattr(-,root,root)
%doc doc/*

