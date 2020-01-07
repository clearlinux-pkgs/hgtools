#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : hgtools
Version  : 8.1.1
Release  : 39
URL      : http://pypi.debian.net/hgtools/hgtools-8.1.1.tar.gz
Source0  : http://pypi.debian.net/hgtools/hgtools-8.1.1.tar.gz
Summary  : Classes and setuptools plugin for Mercurial and Git repositories
Group    : Development/Tools
License  : MIT
Requires: hgtools-python3
Requires: hgtools-python
Requires: Pygments
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest

BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools_scm
BuildRequires : setuptools_scm-python
BuildRequires : tox
BuildRequires : virtualenv

%description
.. image:: https://img.shields.io/pypi/v/hgtools.svg
:target: https://pypi.org/project/hgtools

%package python
Summary: python components for the hgtools package.
Group: Default
Requires: hgtools-python3

%description python
python components for the hgtools package.


%package python3
Summary: python3 components for the hgtools package.
Group: Default
Requires: python3-core

%description python3
python3 components for the hgtools package.


%prep
%setup -q -n hgtools-8.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1528566183
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
