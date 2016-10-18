Summary: Google Drive KIO-slave for KDE applications
Name: kio-gdrive
Version: 1.0.3
Release: 1
License: GPLv2+
Group: Graphical desktop/KDE
Url: http://www.kde.org
Source0: http://download.kde.org/stable/kio-gdrive/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Keychain)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5GAPI)

%description
Google Drive KIO-slave for KDE applications.

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang kio5_gdrive

%files -f kio5_gdrive.lang
