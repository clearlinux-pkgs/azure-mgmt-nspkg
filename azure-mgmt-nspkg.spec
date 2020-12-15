#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : azure-mgmt-nspkg
Version  : 3.0.2
Release  : 6
URL      : https://files.pythonhosted.org/packages/c4/d4/a9a140ee15abd8b0a542c0d31b7212acf173582c10323b09380c79a1178b/azure-mgmt-nspkg-3.0.2.zip
Source0  : https://files.pythonhosted.org/packages/c4/d4/a9a140ee15abd8b0a542c0d31b7212acf173582c10323b09380c79a1178b/azure-mgmt-nspkg-3.0.2.zip
Summary  : Microsoft Azure Resource Management Namespace Package [Internal]
Group    : Development/Tools
License  : MIT
Requires: azure-mgmt-nspkg-python = %{version}-%{release}
Requires: azure-mgmt-nspkg-python3 = %{version}-%{release}
Requires: azure-nspkg
BuildRequires : azure-nspkg
BuildRequires : buildreq-distutils3

%description
==============================
        
        This is the Microsoft Azure Management namespace package.
        
        This package is not intended to be installed directly by the end user.

%package python
Summary: python components for the azure-mgmt-nspkg package.
Group: Default
Requires: azure-mgmt-nspkg-python3 = %{version}-%{release}

%description python
python components for the azure-mgmt-nspkg package.


%package python3
Summary: python3 components for the azure-mgmt-nspkg package.
Group: Default
Requires: python3-core
Provides: pypi(azure_mgmt_nspkg)
Requires: pypi(azure_nspkg)

%description python3
python3 components for the azure-mgmt-nspkg package.


%prep
%setup -q -n azure-mgmt-nspkg-3.0.2
cd %{_builddir}/azure-mgmt-nspkg-3.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588882918
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
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
