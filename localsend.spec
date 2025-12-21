
%global __brp_check_rpaths %{nil}
%global debug_package %{nil}

Name:           localsend
Version:        1.17.0
Release:        1%{?dist}
Summary:        An open source cross-platform alternative to AirDrop
License:        Apache 2.0
URL:            https://localsend.org
Source0:        https://github.com/localsend/localsend/releases/download/v%{version}/LocalSend-%{version}-linux-x86-64.tar.gz

BuildRequires:  desktop-file-utils
Requires:       gtk3
Requires:       libayatana-appindicator-gtk3

%description
LocalSend is a free, open-source application that allows you to securely share files 
and messages with nearby devices over your local network without an internet connection.

%prep
%setup -q -c -n %{name}-%{version}

%build


%install
mkdir -p %{buildroot}%{_libdir}/%{name}
cp -r * %{buildroot}%{_libdir}/%{name}/


mkdir -p %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} <<EOF
#!/bin/bash
exec %{_libdir}/%{name}/localsend_app "\$@"
EOF
chmod +x %{buildroot}%{_bindir}/%{name}


mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=LocalSend
Comment=Share files to nearby devices
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Utility;FileTools;
EOF


mkdir -p %{buildroot}%{_datadir}/icons/hicolor/512x512/apps
find . -name "logo-512.png" -exec cp {} %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/%{name}.png \;

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/512x512/apps/%{name}.png

%changelog
* Sat Dec 20 2025 Vani <vani@example.com> - 1.17.0-1
- Repackaged official binaries for Fedora with RPATH fixes
