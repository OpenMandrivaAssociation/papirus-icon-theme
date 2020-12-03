Name:           papirus-icon-theme
Version:        20201201
Release:        1
Summary:        Free and open source SVG icon theme based on Paper Icon Set

# Some icons are based on Paper Icon Theme, CC-BY-SA
# The rest is GPLv3
License:        GPLv3 and CC-BY-SA
URL:            https://github.com/PapirusDevelopmentTeam/papirus-icon-theme
Source0:        https://github.com/PapirusDevelopmentTeam/papirus-icon-theme/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

%description
Papirus is a free and open source SVG icon theme for Linux, based on Paper
Icon Set with a lot of new icons and a few extras, like Hardcode-Tray support,
KDE colorscheme support, Folder Color support, and others.

Papirus icon theme is available in six variants:

 - Papirus (for Arc / Arc Darker)
 - Papirus Dark (for Arc Dark)
 - Papirus Light (light theme with Breeze colors)
 - Papirus Adapta (for Adapta)
 - Papirus Adapta Nokto (for Adapta Nokto)
 - ePapirus (for elementary OS and Pantheon Desktop)

%prep
%autosetup

%build
# Nothing to build

%install
%make_install

export THEMES="ePapirus Papirus Papirus-Adapta Papirus-Adapta-Nokto Papirus-Dark Papirus-Light"
for t in $THEMES; do
    mkdir -p %{buildroot}%{_datadir}/icons/$t
    /bin/touch %{buildroot}%{_datadir}/icons/$t/icon-theme.cache
done

%post
export THEMES="ePapirus Papirus Papirus-Adapta Papirus-Adapta-Nokto Papirus-Dark Papirus-Light"
for t in $THEMES; do
    /bin/touch --no-create %{_datadir}/icons/$t &>/dev/null || :
done

%postun
export THEMES="ePapirus Papirus Papirus-Adapta Papirus-Adapta-Nokto Papirus-Dark Papirus-Light"
for t in $THEMES; do
    if [ $1 -eq 0 ] ; then
        /bin/touch --no-create %{_datadir}/icons/$t &>/dev/null
        /usr/bin/gtk-update-icon-cache %{_datadir}/icons/$t &>/dev/null || :
    fi
done

%posttrans
export THEMES="ePapirus Papirus Papirus-Adapta Papirus-Adapta-Nokto Papirus-Dark Papirus-Light"
for t in $THEMES; do
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/$t &>/dev/null || :
done

%files
%license LICENSE
%doc AUTHORS README.md
%{_datadir}/icons/ePapirus
%{_datadir}/icons/Papirus
%{_datadir}/icons/Papirus-Adapta
%{_datadir}/icons/Papirus-Adapta-Nokto
%{_datadir}/icons/Papirus-Dark
%{_datadir}/icons/Papirus-Light
%ghost %{_datadir}/icons/ePapirus/icon-theme.cache
%ghost %{_datadir}/icons/Papirus/icon-theme.cache
%ghost %{_datadir}/icons/Papirus-Adapta/icon-theme.cache
%ghost %{_datadir}/icons/Papirus-Adapta-Nokto/icon-theme.cache
%ghost %{_datadir}/icons/Papirus-Dark/icon-theme.cache
%ghost %{_datadir}/icons/Papirus-Light/icon-theme.cache
