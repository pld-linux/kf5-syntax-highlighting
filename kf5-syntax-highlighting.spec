#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeframever	5.109
%define		qtver		5.15.2
%define		kfname		syntax-highlighting

Summary:	Syntax highlighting
Name:		kf5-%{kfname}
Version:	5.109.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	e970abb368b963a075f10f2ef26a95c0
URL:		http://www.kde.org/
BuildRequires:	cmake >= 3.16
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	kf5-dirs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
Syntax highlighting.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON

%ninja_build -C build

%if %{with tests}
%ninja_build -C build test
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang syntaxhighlighting5 --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f syntaxhighlighting5.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kate-syntax-highlighter
%ghost %{_libdir}/libKF5SyntaxHighlighting.so.5
%attr(755,root,root) %{_libdir}/libKF5SyntaxHighlighting.so.5.*.*
%{_datadir}/qlogging-categories5/ksyntaxhighlighting.categories
%{_datadir}/qlogging-categories5/ksyntaxhighlighting.renamecategories
%dir %{_libdir}/qt5/qml/org/kde/syntaxhighlighting
%{_libdir}/qt5/qml/org/kde/syntaxhighlighting/libkquicksyntaxhighlightingplugin.so
%{_libdir}/qt5/qml/org/kde/syntaxhighlighting/qmldir

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KSyntaxHighlighting
%{_libdir}/cmake/KF5SyntaxHighlighting
%{_libdir}/libKF5SyntaxHighlighting.so
%{_libdir}/qt5/mkspecs/modules/qt_KSyntaxHighlighting.pri
