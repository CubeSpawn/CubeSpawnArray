#!/bin/bash

cd ~
# Base directory name
BASE_DIR="CubeSpawnArray"

# Create base directory
mkdir -p $BASE_DIR

# Create the main directory structure
mkdir -p $BASE_DIR/src/core/machine_tools
mkdir -p $BASE_DIR/src/core/conveyors/pico_deployment
mkdir -p $BASE_DIR/src/core/sensors
mkdir -p $BASE_DIR/src/ros_integration/ros_configs
mkdir -p $BASE_DIR/src/linuxcnc_integration/cnc_configs
mkdir -p $BASE_DIR/src/octoprint_integration
mkdir -p $BASE_DIR/src/machinekit_integration
mkdir -p $BASE_DIR/src/erp_integration
mkdir -p $BASE_DIR/src/management_pc/ui
mkdir -p $BASE_DIR/src/management_pc/operations
mkdir -p $BASE_DIR/src/logging
mkdir -p $BASE_DIR/src/log_parsing
mkdir -p $BASE_DIR/src/performance_analysis
mkdir -p $BASE_DIR/src/ml_applications/models
mkdir -p $BASE_DIR/src/ml_applications/training
mkdir -p $BASE_DIR/src/database/migrations
mkdir -p $BASE_DIR/src/tests

# New directories for controller PC, management PC, and WebGUI
mkdir -p $BASE_DIR/src/controller_pc/ansible_scripts
mkdir -p $BASE_DIR/src/controller_pc/monitoring
mkdir -p $BASE_DIR/src/controller_pc/deployment
mkdir -p $BASE_DIR/src/controller_pc/MQTT
mkdir -p $BASE_DIR/src/management_pc/gui_tools/tkinter
mkdir -p $BASE_DIR/src/webgui/{templates,static/{css,js,images}}

mkdir -p $BASE_DIR/docs
mkdir -p $BASE_DIR/config
mkdir -p $BASE_DIR/deployment/ansible_playbooks
mkdir -p $BASE_DIR/deployment/pico_deployment
mkdir -p $BASE_DIR/scripts
mkdir -p $BASE_DIR/venv

# Create files in base directories
touch $BASE_DIR/README.md
touch $BASE_DIR/requirements.txt
touch $BASE_DIR/setup.py
touch $BASE_DIR/.gitignore

# Create __init__.py in each Python package directory
find $BASE_DIR/src -type d -exec touch {}/__init__.py \;

# Create placeholder Python scripts
touch $BASE_DIR/src/core/control_system.py
touch $BASE_DIR/src/core/conveyors/pico_deployment/deploy_pico.py
touch $BASE_DIR/src/ros_integration/{ros_nodes.py,ros_services.py}
touch $BASE_DIR/src/linuxcnc_integration/{lathe_cnc.py,mill_cnc.py}
touch $BASE_DIR/src/octoprint_integration/printer_control.py
touch $BASE_DIR/src/machinekit_integration/{mill_drill_control.py,cold_saw_control.py}
touch $BASE_DIR/src/erp_integration/{erp_connector.py,database.py}
touch $BASE_DIR/src/management_pc/ui/{main_ui.py,settings_ui.py}
touch $BASE_DIR/src/management_pc/operations/{scheduling.py,monitoring.py}
touch $BASE_DIR/src/logging/{mtconnect_logs.py,mqtt_logs.py,ros_logs.py,octoprint_logs.py}
touch $BASE_DIR/src/log_parsing/{parser_mtconnect.py,parser_mqtt.py,parser_ros.py,parser_octoprint.py,standardizer.py}
touch $BASE_DIR/src/performance_analysis/analysis.py
touch $BASE_DIR/src/ml_applications/models/{predictive_maintenance.py,anomaly_detection.py}
touch $BASE_DIR/src/ml_applications/training/train_model.py
touch $BASE_DIR/src/database/models.py

# Placeholder scripts for controller PC, management PC, and WebGUI
touch $BASE_DIR/src/controller_pc/monitoring/monitor_logs.py
touch $BASE_DIR/src/controller_pc/deployment/deploy_control.py
touch $BASE_DIR/src/management_pc/gui_tools/tkinter/{tool1.py,tool2.py}
touch $BASE_DIR/src/webgui/flask_app.py

# Create example config files
touch $BASE_DIR/config/{config.yaml,database.ini,ros_config.yaml,linuxcnc_config.yaml,machinekit_config.yaml,octoprint_config.yaml}

# Create example deployment scripts
touch $BASE_DIR/deployment/ansible_playbooks/{deploy_rpi.yml,deploy_machinekit.yml}
touch $BASE_DIR/deployment/pico_deployment/deploy_pico.py

# Create example scripts
touch $BASE_DIR/scripts/{setup_db.py,start_ros.py,start_linuxcnc.py,start_octoprint.py,start_machinekit.py}

echo "Directory structure for CubeSpawnArray created successfully."

