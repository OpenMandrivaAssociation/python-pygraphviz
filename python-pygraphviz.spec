%define module	pygraphviz

Summary:	Python interface to Graphviz
Name:		python2-%{module}
Version:	1.2
Release:	3
Source0:	https://pypi.python.org/packages/source/p/pygraphviz/pygraphviz-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://networkx.lanl.gov/pygraphviz
Requires:	graphviz >= 2.0
BuildRequires:	graphviz-devel >= 2.0
BuildRequires:	python2-devel
BuildRequires:	python2-sphinx

%description
PyGraphviz is a Python interface to the Graphviz graph layout and
visualization package.

With PyGraphviz, you can create, edit, read, write, and draw graphs
using Python to access the Graphviz graph data structure and layout
algorithms.

%prep
%setup -q -n %{module}-%{version}

%build
PYTHONDONTWRITEBYTECODE= %__python2 setup.py build
pushd doc
export PYTHONPATH=`dir -d ../build/lib.linux*`
%make html SPHINXBUILD=sphinx-build2
popd

%install
PYTHONDONTWRITEBYTECODE= %__python2 setup.py install --root=%{buildroot} --record=FILE_LIST
sed -i 's/.*examples$//' FILE_LIST

%files -f FILE_LIST
%doc doc/build/html



%changelog
* Wed Jun 01 2011 Lev Givon <lev@mandriva.org> 1.1-1mdv2011.0
+ Revision: 682332
- Update to 1.1.

* Thu May 12 2011 Lev Givon <lev@mandriva.org> 1.1-0.rc1.1
+ Revision: 673900
- Update to 1.1rc1.

* Wed May 11 2011 Funda Wang <fwang@mandriva.org> 1.0-0.rc6.1
+ Revision: 673621
- add source
- rebuild for new graphviz

* Mon Nov 08 2010 Funda Wang <fwang@mandriva.org> 1.0-0.rc5.1mdv2011.0
+ Revision: 594961
- BR python devel
- rebuild

* Fri Jul 30 2010 Lev Givon <lev@mandriva.org> 1.0-0.rc5mdv2011.0
+ Revision: 563641
- Update to 1.0rc5.

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.99.1-3mdv2010.0
+ Revision: 442429
- rebuild

* Sun Dec 28 2008 Funda Wang <fwang@mandriva.org> 0.99.1-2mdv2009.1
+ Revision: 320200
- fix str fmt
- rebuild for new python

* Sun Dec 14 2008 Lev Givon <lev@mandriva.org> 0.99.1-1mdv2009.1
+ Revision: 314214
- Update to 0.99.1.

* Mon Jul 07 2008 Lev Givon <lev@mandriva.org> 0.36-1mdv2009.0
+ Revision: 232507
- import python-pygraphviz


* Mon Jul 7 2008 Lev Givon <lev@mandriva.org> 0.36-1mdv2008.1
- Package for Mandriva.

