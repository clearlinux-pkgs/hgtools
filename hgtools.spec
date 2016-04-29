#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : hgtools
Version  : 6.3
Release  : 9
URL      : https://pypi.python.org/packages/source/h/hgtools/hgtools-6.3.zip
Source0  : https://pypi.python.org/packages/source/h/hgtools/hgtools-6.3.zip
Summary  : Classes and setuptools plugin for Mercurial repositories
Group    : Development/Tools
License  : MIT
Requires: hgtools-python
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
hgtools
=======
hgtools builds on the setuptools_hg plugin for setuptools. hgtools
provides classes for inspecting and working with repositories in the
Mercurial and Git version control systems (VCS).

%package python
Summary: python components for the hgtools package.
Group: Default

%description python
python components for the hgtools package.


%prep
%setup -q -n hgtools-6.3

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
