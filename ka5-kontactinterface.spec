%define		kdeappsver	21.04.3
%define		kframever	5.56.0
%define		kfver		5.53.0
%define		qtver		5.9.0
%define		kaname		kontactinterface
Summary:	Kontact interface
Name:		ka5-%{kaname}
Version:	21.04.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	f7c09305dd10b6f6b87ba7cddadd99bf
URL:		http://www.kde.org/
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kiconthemes-devel >= %{kframever}
BuildRequires:	kf5-kparts-devel >= %{kframever}
BuildRequires:	kf5-kwindowsystem-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kontact interface.

%description -l pl.UTF-8
Interfejs programowy do Kontact.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build
install -d $RPM_BUILD_ROOT%{_includedir}/KF5/Akonadi

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%ghost %{_libdir}/libKF5KontactInterface.so.5
%attr(755,root,root) %{_libdir}/libKF5KontactInterface.so.*.*.*
%{_datadir}/kservicetypes5/kontactplugin.desktop
%{_datadir}/qlogging-categories5/kontactinterface.categories
%{_datadir}/qlogging-categories5/kontactinterface.renamecategories

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KontactInterface
%{_includedir}/KF5/kontactinterface_version.h
%{_libdir}/cmake/KF5KontactInterface
%{_libdir}/libKF5KontactInterface.so
%{_libdir}/qt5/mkspecs/modules/qt_KontactInterface.pri
