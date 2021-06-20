%global release_prefix          101

Name:                           discord
Version:                        0.0.15
Release:                        %{release_prefix}%{?dist}
Summary:                        Discord is a proprietary freeware VoIP application
License:                        Proprietary
URL:                            https://discordapp.com
Vendor:                         Package Store <https://pkgstore.github.io>
Packager:                       Kitsune Solar <kitsune.solar@gmail.com>

Source0:                        https://dl.discordapp.net/apps/linux/%{version}/%{name}-%{version}.tar.gz
Source10:                       Discord.desktop

BuildRequires:                  libXScrnSaver libcxx libatomic
Requires:                       libXScrnSaver libcxx libatomic
AutoReqProv:                    no

%description
Discord is a proprietary freeware VoIP application and digital
distribution platform designed for video gaming communities, that
specializes in text, image, video and audio communication between
users in a chat channel.

%global debug_package %{nil}

# -------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------------------< SCRIPT >----------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

%prep
%autosetup -n Discord


%build


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_bindir}/
%{__mkdir_p} %{buildroot}/opt/Discord
%{__mkdir_p} %{buildroot}/usr/share/applications

%{__cp} -r * %{buildroot}/opt/Discord/
%{__ln_s} -f /opt/Discord/Discord %{buildroot}%{_bindir}/
%{__install} -Dp -m 755 %{SOURCE10} %{buildroot}%{_datadir}/applications/Discord.desktop


%files
%defattr(-,root,root)
/opt/Discord/
%{_bindir}/Discord
%{_datadir}/applications/Discord.desktop


%clean
rm -rf %{buildroot}


%changelog
* Sun Jun 20 2021 Package Store <kitsune.solar@gmail.com> - 0.0.15-101
- FIX: Discord icon.

* Sun Jun 20 2021 Package Store <kitsune.solar@gmail.com> - 0.0.15-100
- UPD: Move to GitHub.
- UPD: License.

* Mon Mar 30 2020 Package Store <kitsune.solar@gmail.com> - 0.0.10-101
- FIX: Error "Discord installation is corrupt".

* Fri Mar 27 2020 Package Store <kitsune.solar@gmail.com> - 0.0.10-100
- NEW: v0.0.10.
