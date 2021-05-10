%define		kdeframever	5.82
%define		qtver		5.9.0
%define		kfname		syntax-highlighting

Summary:	Syntax highlighting
Name:		kf5-%{kfname}
Version:	5.82.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	6c347e612a4f4cfab64e47e59ea028af
URL:		http://www.kde.org/
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
install -d build
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%ninja_build

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

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KSyntaxHighlighting
%{_includedir}/KF5/ksyntaxhighlighting_version.h
%{_libdir}/cmake/KF5SyntaxHighlighting
%{_libdir}/libKF5SyntaxHighlighting.so
%{_libdir}/qt5/mkspecs/modules/qt_KSyntaxHighlighting.pri
