Name:       qt5-qtmultimedia-plugin-mediaservice-irisradio

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary:    Qt Multimedia - Iris FM Radio media service
Version:    0.6.0
Release:    1%{?dist}
License:    LGPLv2+
URL:        https://github.com/mer-hybris/qt5-qtmultimedia-plugin-mediaservice-irisradio
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qmake
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Multimedia)

%description
Qt5 Iris FM Radio media service plugin


%prep
%setup -q -n %{name}-%{version}

%build

%qtc_qmake5

%qtc_make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%qmake5_install

rm -f %{buildroot}/usr/lib/cmake/Qt5Multimedia/Qt5Multimedia_FMRadioServicePlugin.cmake

%files
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/qt5/plugins/mediaservice/libqtmedia_irisradio.so
