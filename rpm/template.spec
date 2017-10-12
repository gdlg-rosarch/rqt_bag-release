Name:           ros-lunar-rqt-bag-plugins
Version:        0.4.9
Release:        0%{?dist}
Summary:        ROS rqt_bag_plugins package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/rqt_bag
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       pycairo
Requires:       python-pillow
Requires:       python-pillow-qt
Requires:       ros-lunar-geometry-msgs
Requires:       ros-lunar-rosbag
Requires:       ros-lunar-roslib
Requires:       ros-lunar-rospy
Requires:       ros-lunar-rqt-bag
Requires:       ros-lunar-rqt-gui
Requires:       ros-lunar-rqt-gui-py
Requires:       ros-lunar-rqt-plot
Requires:       ros-lunar-sensor-msgs
Requires:       ros-lunar-std-msgs
BuildRequires:  ros-lunar-catkin

%description
rqt_bag provides a GUI plugin for displaying and replaying ROS bag files.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Thu Oct 12 2017 Dirk Thomas <dthomas@osrfoundation.org> - 0.4.9-0
- Autogenerated by Bloom

* Mon Apr 24 2017 Dirk Thomas <dthomas@osrfoundation.org> - 0.4.8-0
- Autogenerated by Bloom

