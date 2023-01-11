// Copyright 2018-2018 the openage authors. See copying.md for legal info.

#include "terrain.h"

#include "renderer/stages/terrain/terrain_render_entity.h"

namespace openage::gamestate {

Terrain::Terrain(util::Path &texture_path) :
	size{0, 0},
	height_map{},
	texture_path{texture_path},
	render_entity{nullptr} {
	// TODO
}

void Terrain::push_to_render() {
	if (this->render_entity != nullptr) {
		this->render_entity->update(this->size,
		                            this->height_map,
		                            this->texture_path);
	}
}

void Terrain::set_render_entity(const std::shared_ptr<renderer::terrain::TerrainRenderEntity> &entity) {
	this->render_entity = entity;

	this->push_to_render();
}

} // namespace openage::gamestate
