%define		kdeframever	5.39
%define		qtver		5.3.2
%define		kfname		syntax-highlighting

Summary:	Syntax highlighting
Name:		kf5-%{kfname}
Version:	5.39.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	f50176753c157333fbd566a27bb6d205
URL:		http://www.kde.org/
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
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT

%find_lang syntaxhighlighting5 --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f syntaxhighlighting5.lang
%defattr(644,root,root,755)
/etc/xdg/org_kde_ksyntaxhighlighting.categories
%attr(755,root,root) %{_bindir}/kate-syntax-highlighter
%attr(755,root,root) %ghost %{_libdir}/libKF5SyntaxHighlighting.so.5
%attr(755,root,root) %{_libdir}/libKF5SyntaxHighlighting.so.5.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KSyntaxHighlighting
%{_includedir}/KF5/ksyntaxhighlighting_version.h
%{_libdir}/cmake/KF5SyntaxHighlighting
%{_libdir}/libKF5SyntaxHighlighting.so
%{_libdir}/qt5/mkspecs/modules/qt_KSyntaxHighlighting.pri
